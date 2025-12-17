---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsdeviceregistration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsDeviceRegistration
---

# 设置 AdfsDeviceRegistration

## 摘要
配置设备注册服务的管理策略。

## 语法

### NumberOfInactiveDays（非活跃天数）
```
Set-AdfsDeviceRegistration -MaximumInactiveDays <UInt32> [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 每用户设备数量（NumberOfDevicesPerUser）
```
Set-AdfsDeviceRegistration -DevicesPerUser <UInt32> [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ServiceAccountIdentifier
```
Set-AdfsDeviceRegistration -ServiceAccountIdentifier <String> -Credential <PSCredential>
 [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 发行证书（IssuanceCertificate）
```
Set-AdfsDeviceRegistration [-IssuanceCertificate] [-AccessControlPolicyName <String>]
 [-AccessControlPolicyParameters <Object>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RelyingParty（依赖方）
```
Set-AdfsDeviceRegistration [-AccessControlPolicyName <String>] [-AccessControlPolicyParameters <Object>]
 [-AllowedAuthenticationClassReferences <String[]>] [-IssuanceAuthorizationRules <String>]
 [-IssuanceAuthorizationRulesFile <String>] [-IssuanceTransformRules <String>]
 [-IssuanceTransformRulesFile <String>] [-AdditionalAuthenticationRules <String>]
 [-AdditionalAuthenticationRulesFile <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsDeviceRegistration` cmdlet 用于配置设备注册服务的管理策略。您可以使用此 cmdlet 来更改 Active Directory Federation Services (AD FS) 中设备注册服务的默认策略，例如用户可以注册的最大设备数量。

## 示例

### 示例 1：设置用户可以注册的设备数量
```
PS C:\> Set-AdfsDeviceRegistration -DevicesPerUser 10
```

该命令将用户可以注册的设备数量限制为10个。

### 示例 2：配置设备的最长非活动天数
```
PS C:\> Set-AdfsDeviceRegistration -MaximumInactiveDays 90
```

该命令用于配置设备注册服务在删除非活跃设备对象之前的天数间隔。

### 示例 3：为设备注册服务设置服务账户
```
PS C:\> $Cred = Get-Credential
PS C:\> Set-AdfsDeviceRegistration -ServiceAccountIdentifier "CONTOSO\Svc_adfs" -Credential $Cred
```

第一个命令使用了 **Get-Credential** cmdlet 来为运行 AD FS 服务的 Active Directory 账户创建一个凭据对象。该命令将凭据对象存储在 `$Cred` 变量中。

第二个命令用于设置服务账户，该账户的ID为Svc_adfs。该命令指定了存储在$Cred中的凭据信息，这些凭据用于运行AD FS服务的Active Directory账户。

## 参数

### -AccessControlPolicyName
```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AccessControlPolicyParameters
```yaml
Type: Object
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AdditionalAuthenticationRules
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -AdditionalAuthenticationRulesFile
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowedAuthenticationClassReferences
```yaml
Type: String[]
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
```yaml
Type: PSCredential
Parameter Sets: ServiceAccountIdentifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DevicesPerUser
指定用户可以注册的最大设备数量。

```yaml
Type: UInt32
Parameter Sets: NumberOfDevicesPerUser
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IssuanceAuthorizationRules
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IssuanceAuthorizationRulesFile
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IssuanceCertificate
表示该cmdlet为设备注册服务生成并使用一个新的签名证书。

```yaml
Type: SwitchParameter
Parameter Sets: IssuanceCertificate
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IssuanceTransformRules
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -IssuanceTransformRulesFile
```yaml
Type: String
Parameter Sets: RelyingParty
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaximumInactiveDays
指定由于设备长时间不活动而被删除之前的天数。

```yaml
Type: UInt32
Parameter Sets: NumberOfInactiveDays
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ServiceAccountIdentifier
指定服务账户的ID。该cmdlet为该账户提供对Active Directory® Domain Services中的设备注册服务配置文件及相关容器的读写访问权限。

```yaml
Type: String
Parameter Sets: ServiceAccountIdentifier
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### uint

### 字符串

### SwitchParameter

## 输出

## 备注

## 相关链接

[禁用 Adfs 设备注册功能](./Disable-AdfsDeviceRegistration.md)

[Enable-AdfsDeviceRegistration](./Enable-AdfsDeviceRegistration.md)

[Get-AdfsDeviceRegistration](./Get-AdfsDeviceRegistration.md)

