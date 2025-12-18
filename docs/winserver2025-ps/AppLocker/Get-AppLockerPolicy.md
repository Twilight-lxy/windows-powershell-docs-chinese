---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.dll-Help.xml
Module Name: AppLocker
ms.date: 09/28/2020
online version: https://learn.microsoft.com/powershell/module/applocker/get-applockerpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppLockerPolicy
---

# 获取 AppLocker 策略

## 摘要
获取本地、生效的或域级别的 AppLocker 策略。

## 语法

### LocalPolicy（默认值）
```
Get-AppLockerPolicy [-Local] [-Xml] [<CommonParameters>]
```

### DomainPolicy
```
Get-AppLockerPolicy [-Domain] -Ldap <String> [-Xml] [<CommonParameters>]
```

### EffectivePolicy
```
Get-AppLockerPolicy [-Effective] [-Xml] [<CommonParameters>]
```

## 描述
`Get-AppLockerPolicy` cmdlet 从本地组策略对象（GPO）、指定的 GPO 或计算机上部署的有效组策略中检索 AppLocker 策略。

默认情况下，输出结果是一个 **AppLockerPolicy** 对象。如果使用了 *Xml* 参数，那么输出结果将以 XML 格式的字符串形式呈现该 AppLocker 策略。

请注意，Get-AppLockerPolicy cmdlet 仅适用于通过 Group Policy (GP) 部署的 AppLocker 策略。该 cmdlet 不了解 AppLocker Cloud Service Provider (CSP) 的工作原理；因此，如果实际应用的策略是通过 CSP 部署的，它将返回错误的数据。

## 示例

### 示例 1：获取 AppLocker 策略
```
PS C:\> Get-AppLockerPolicy -Local
                                Version RuleCollections                         RuleCollectionTypes
                                ------- ---------------                         -------------------
                                      1 {}                                      {}
```

这个示例将本地的 AppLocker 策略获取为一个 **AppLockerPolicy** 对象。

### 示例 2：获取某个 GPO 的 AppLocker 策略
```
PS C:\> Get-AppLockerPolicy -Domain -LDAP "LDAP:// DC13.Contoso.com/CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=Contoso,DC=com"
```

这个示例将通过 LDAP 路径指定的唯一 GPO 的 AppLocker 策略获取为一个 **AppLockerPolicy** 对象。

#### 示例 3：获取生效的政策
```
PS C:\> Get-AppLockerPolicy -Effective -Xml | Set-Content ('c:\temp\curr.xml')
```

这个示例会获取计算机上的有效策略，然后将其以XML格式发送到指定路径下的文件中。

### 示例 4：获取并测试 AppLocker 策略
```
PS C:\> Get-AppLockerPolicy -Local | Test-AppLockerPolicy -Path C:\Windows\System32\*.exe -User Everyone
```

这个示例会获取计算机上的本地 AppLocker 策略，然后使用 **Test-AppLockerPolicy** cmdlet 来测试该策略：具体来说，它会检查 C:\Windows\System32 目录中的 .exe 文件是否会被 “Everyone” 组允许运行。

## 参数

### -Domain
从由*Ldap*参数中指定的路径所对应的GPO（组策略对象）中获取AppLocker策略。

```yaml
Type: SwitchParameter
Parameter Sets: DomainPolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Effective
获取本地计算机上有效的AppLocker策略。该有效策略是本地AppLocker策略与本地计算机上应用的任何AppLocker域策略的合并结果。

```yaml
Type: SwitchParameter
Parameter Sets: EffectivePolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Ldap
指定 GPO 的 LDAP 路径，并且必须指定一个唯一的 GPO。

```yaml
Type: String
Parameter Sets: DomainPolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Local
从本地的组策略对象（GPO）中获取 AppLocker 策略。

```yaml
Type: SwitchParameter
Parameter Sets: LocalPolicy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Xml
指定将 AppLocker 策略输出为 XML 格式的字符串。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.AppLockerPolicy
**AppLockerPolicy**

### System.String

## 备注

## 相关链接

[Get-AppLockerFileInformation](./Get-AppLockerFileInformation.md)

[New-AppLockerPolicy](./New-AppLockerPolicy.md)

[Set-AppLockerPolicy](./Set-AppLockerPolicy.md)

[测试-AppLockerPolicy](./Test-AppLockerPolicy.md)

