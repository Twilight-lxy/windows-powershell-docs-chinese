---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.dll-Help.xml
Module Name: AppLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/applocker/new-applockerpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AppLockerPolicy
---

# 新的AppLocker策略

## 摘要
根据文件信息列表及其他规则创建选项来生成一个新的 AppLocker 策略。

## 语法

### 文件信息
```
New-AppLockerPolicy
 [-FileInformation] <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.FileInformation]>
 [-AllowWindows]
 [-RuleType <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.RuleType]>]
 [-RuleNamePrefix <String>] [-User <String>] [-Optimize] [-IgnoreMissingFileInformation] [-Xml]
 [-ServiceEnforcement <ServiceEnforcementMode>] [<CommonParameters>]
```

### AllowWindows
```
New-AppLockerPolicy [-AllowWindows]
 [-RuleType <System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.RuleType]>]
 [-RuleNamePrefix <String>] [-User <String>] [-Optimize] [-IgnoreMissingFileInformation] [-Xml]
 [-ServiceEnforcement <ServiceEnforcementMode>] [<CommonParameters>]
```

## 描述
`New-AppLockerPolicy` cmdlet 使用文件信息列表来为指定的用户或组自动生成规则列表。规则可以根据发行商、哈希值或路径信息进行生成。

运行 `Get-AppLockerFileInformation` cmdlet 以创建文件信息列表。

默认情况下，输出结果是一个 **AppLockerPolicy** 对象。如果指定了 *Xml* 参数，那么输出结果将是以 XML 格式表示的 AppLocker 策略字符串。

## 示例

### 示例 1：创建包含允许规则的 AppLocker 策略
```
C:\PS>Get-ChildItem C:\Windows\System32\*.exe | Get-AppLockerFileInformation | New-AppLockerPolicy -RuleType Publisher, Hash -User Everyone -RuleNamePrefix System32

                                Version RuleCollections                         RuleCollectionTypes
                                ------- ---------------                         -------------------
                                      1 {Microsoft.Security.ApplicationId.Po... {Exe}
```

这个示例创建了一个 AppLocker 策略，其中包含针对 C:\Windows\System32 目录下所有可执行文件的允许规则。对于那些具有发布者信息的文件，该策略还包含了相应的发布者规则；而对于没有发布者信息的文件，则包含了哈希规则。这些规则的前缀为 `System32:`，并且这些规则适用于 “Everyone” 组用户。

### 示例 2：创建一个 AppLocker 策略
```
C:\PS>Get-ChildItem C:\Windows\System32\*.exe | Get-AppLockerFileInformation | New-AppLockerPolicy -AllowWindows -RuleType Path -User Everyone -Optimize -XML
<AppLockerPolicy Version="1"><RuleCollection Type="Exe" EnforcementMode="NotConfigured"><FilePathRule Id="31B2F340-016D
-11D2-945F-00C04FB984F9" Name="%SYSTEM32%\*" Description="" 10 UserOrGroupSid="S-1-5-21-3165297888-301567370-576410423-
13" Action="cAllow"><Conditions><FilePathCondition Path="%SYSTEM32%\*" /></Conditions></FilePathRule></RuleCollection>
</AppLockerPolicy>
```

这个示例为 `C:\Windows\System32` 目录下的所有可执行文件创建了一个 XML 格式的 AppLocker 策略。该策略仅包含路径规则，并且这些规则适用于 “Everyone” 组。`Optimize` 参数表示在可能的情况下，相似的规则会被合并到一起。此外，此 AppLocker 策略信任所有的本地 Windows 组件。

### 示例 3：根据审核后的事件创建一个 AppLocker 策略
```
C:\PS>Get-AppLockerFileInformation -EventLog -LogPath "Microsoft-Windows-AppLocker/EXE and DLL" -EventType Audited | New-AppLockerPolicy -RuleType Publisher,Hash -User domain\FinanceGroup -IgnoreMissingFileInformation | Set-AppLockerPolicy -LDAP "LDAP://DC13.TailspinToys.com/CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=WingTipToys,DC=com"
```

这个示例根据本地“Microsoft-Windows-AppLocker/EXE”和“DLL”事件日志中记录的审计事件创建一个新的AppLocker策略。所有规则都将应用于“Domain\FinanceGroup”组。当发布者信息可用时，会生成相应的“发布者规则”；如果发布者信息缺失，则会生成“哈希规则”。对于那些只有文件路径信息的文件，由于指定了“IgnoreMissingFileInformation”参数，这些文件将被忽略，并会被记录到警告日志中。如果在缺少文件信息的情况下没有指定该参数，那么该cmdlet将无法创建相应的规则类型并因此退出执行。新AppLocker策略创建完成后，会将该策略应用到指定的组策略对象（Group Policy Object, GPO）中，从而覆盖该GPO中现有的AppLocker策略。

## 参数

### -AllowWindows
表示 AppLocker 策略允许使用所有本地的 Windows 组件。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileInformation
指定一个文件，该文件可以包含发布者、路径和哈希信息。某些信息可能会缺失，例如未签名文件的发布者信息。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.FileInformation]
Parameter Sets: FileInformation
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -IgnoreMissingFileInformation
说明：如果由于缺少文件信息而无法为某个文件创建规则，那么系统将继续评估该文件的其余信息，并生成一个包含被跳过文件的警告日志。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Optimize
指定相似的规则将被归为一组。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RuleNamePrefix
指定一个名称，作为每个创建的规则的前缀。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RuleType
指定根据文件信息创建的规则类型。可以从文件信息中创建发布者（Publisher）规则、路径（Path）规则或哈希（Hash）规则。可以指定多种规则类型；如果所需的文件信息不可用，系统也会提供相应的备份规则类型。

例如，如果为该参数指定了“Publisher, Hash”，那么当出版商信息不可用时，就会应用哈希规则。

```yaml
Type: System.Collections.Generic.List`1[Microsoft.Security.ApplicationId.PolicyManagement.RuleType]
Parameter Sets: (All)
Aliases:
Accepted values: Publisher, Path, Hash

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceEnforcement
指定 AppLocker 策略（针对 EXE 和 DLL 规则集）是否适用于非交互式进程。该参数的合法取值如下：

- NotConfigured
- Enabled
- ServicesOnly

```yaml
Type: ServiceEnforcementMode
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User
指定规则将应用于哪个用户或组。该参数的可接受值包括：

- DNS user name (domain\username)
- User Principal Name (username@domain.com)
- SAM user name (username)
- Security identifier (S-1-5-21-3165297888-301567370-576410423-1103)

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Xml
指定 AppLocker 策略的输出应为 XML 格式的字符串。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.security.ApplicationId.PolicyManagement.PolicyModel.FileInformation

## 输出

### Microsoft SECURITY.ApplicationId.PolicyManagement.PolicyModel.AppLockerPolicy

### System.String

## 备注

## 相关链接

[Get-AppLockerFileInformation](./Get-AppLockerFileInformation.md)

[Get-AppLockerPolicy](./Get-AppLockerPolicy.md)

[Set-AppLockerPolicy](./Set-AppLockerPolicy.md)

[测试 AppLockerPolicy](./Test-AppLockerPolicy.md)

