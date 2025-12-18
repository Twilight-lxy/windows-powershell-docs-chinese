---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Security.ApplicationId.PolicyManagement.Cmdlets.dll-Help.xml
Module Name: AppLocker
ms.date: 09/28/2020
online version: https://learn.microsoft.com/powershell/module/applocker/set-applockerpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AppLockerPolicy
---

# 设置 AppLocker 策略

## 摘要
为指定的组策略对象（GPO）设置 AppLocker 策略。

## 语法

### ByXmlPolicy（默认值）
```
Set-AppLockerPolicy [-XmlPolicy] <String> [-Ldap <String>] [-Merge] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ByPolicyObject
```
Set-AppLockerPolicy [-PolicyObject] <AppLockerPolicy> [-Ldap <String>] [-Merge] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AppLockerPolicy` cmdlet 用于将指定的 GPO 设置为包含所指定的 AppLocker 策略。如果没有指定轻量级目录访问协议（LDAP），则默认使用本地 GPO。

AppLocker策略的输入值可以是一个`AppLockerPolicy`对象，或者是一个包含AppLocker策略内容的XML格式文件。

请注意，Set-AppLockerPolicy cmdlet 仅适用于组策略（Group Policy，简称 GP），无法与 AppLocker Content Protection Service（AppLocker CSP）进行交互。

## 示例

#### 示例 1：设置本地的 AppLocker 策略
```
PS C:\> Set-AppLockerPolicy -XMLPolicy C:\Policy.xml
```

这个示例将本地的 AppLocker 策略设置为 C:\Policy.xml 文件中指定的策略。

### 示例 2：将 GPO 设置为包含 AppLocker 策略。
```
PS C:\> Set-AppLockerPolicy -XMLPolicy C:\Policy.xml -LDAP "LDAP://DC13.Contoso.com/CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=Contoso,DC=com"
```

这个示例将 LDAP 路径中指定的 GPO 设置为包含位于 C:\Policy.xml 中的 AppLocker 策略。

### 示例 3：将本地的 AppLocker 策略与另一个策略合并
```
PS C:\> Get-AppLockerPolicy -Local | Set-AppLockerPolicy -LDAP "LDAP://DC13.Contoso.com/CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=Contoso,DC=com" -Merge
```

这个示例会获取本地的 AppLocker 策略，然后将该策略与 LDAP 路径中指定的 GPO 中现有的 AppLocker 策略合并。有关如何合并两个策略的更多信息，请参阅 *Merge* 参数的描述。

## 参数

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Ldap
指定 GPO 的 LDAP 路径。必须指定一个唯一的 GPO。如果未指定此参数，则会应用本地 AppLocker 策略。

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

### -Merge
将指定的 AppLocker 策略中的规则与 LDAP 路径中指定的目标 GPO 中的 AppLocker 规则合并。合并规则时会删除具有重复规则 ID 的规则，并保留目标 GPO 中由 AppLocker 策略指定的强制设置。如果未指定 *Merge* 参数，则新策略将覆盖现有策略。

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

### -PolicyObject
指定包含 AppLocker 策略的 **AppLockerPolicy** 对象。可以通过 Get-AppLockerPolicy 和 New-AppLockerPolicy cmdlet 获取该对象。

```yaml
Type: AppLockerPolicy
Parameter Sets: ByPolicyObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并未被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -XmlPolicy
指定保存包含 AppLocker 策略的 XML 格式文件的路径。

```yaml
Type: String
Parameter Sets: ByXmlPolicy
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Security.ApplicationId.PolicyManagement.PolicyModel.AppLockerPolicy
**AppLockerPolicy**

### System.String

## 输出

### 无

## 备注

## 相关链接

[Get-AppLockerFileInformation](./Get-AppLockerFileInformation.md)

[Get-AppLockerPolicy](./Get-AppLockerPolicy.md)

[New-AppLockerPolicy](./New-AppLockerPolicy.md)

[测试 AppLockerPolicy](./Test-AppLockerPolicy.md)

