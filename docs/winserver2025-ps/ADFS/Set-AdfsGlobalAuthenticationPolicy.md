---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsglobalauthenticationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsGlobalAuthenticationPolicy
---

# 设置 AdfsGlobalAuthenticationPolicy

## 摘要
修改 AD FS 全局策略。

## 语法

```
Set-AdfsGlobalAuthenticationPolicy [-AdditionalAuthenticationProvider <String[]>]
 [-DeviceAuthenticationEnabled <Boolean>] [-DeviceAuthenticationMethod <DeviceAuthenticationMethod>]
 [-AllowDeviceAuthAsPrimaryForDomainJoinedDevices <Boolean>]
 [-PrimaryExtranetAuthenticationProvider <String[]>] [-PrimaryIntranetAuthenticationProvider <String[]>]
 [-WindowsIntegratedFallbackEnabled <Boolean>] [-ClientAuthenticationMethods <ClientAuthenticationMethod>]
 [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsGlobalAuthenticationPolicy` 这个 cmdlet 用于修改 Active Directory Federation Services (AD FS) 的全局策略。您还可以使用该 cmdlet 在全局策略中启用外部提供者。

## 示例

### 示例 1：设置主要的外联网身份验证策略
```
PS C:\> Set-AdfsGlobalAuthenticationPolicy -PrimaryExtranetAuthenticationProvider @('FormsAuthentication', 'CertificateAuthentication')
```

此命令将主要的外网身份验证策略设置为基于表单的身份验证或基于证书的身份验证。在这种情况下，当用户从外网登录到由 AD FS 保护的应用程序时，系统会提供相应的身份验证方式供用户选择。

### 示例 2：启用额外的身份验证提供者
```
PS C:\> Set-AdfsGlobalAuthenticationPolicy -AdditionalAuthenticationProvider "A1ExternalAuthProvider"
```

此命令将名为 A1ExternalAuthProvider 的提供程序设置为全局策略中的另一个身份验证提供程序。请注意，*AdditionalAuthenticationProvider* 参数所设置的值应与在 **Register-AdfsAuthenticationProvider** cmdlet 中为 *Name* 参数提供的值相匹配，同时也应与 **Get-AdfsAuthenticationProvider** cmdlet 输出结果中的 **Name** 属性相匹配。

## 参数

### -AdditionalAuthenticationProvider
指定一个外部身份验证提供者的名称数组，以便将其添加到全局策略中。

指定此参数会在全局策略中配置一个用于第二阶段身份验证的外部认证提供者。这是创建一个能够调用外部认证提供者以实现多因素身份验证的 AD FS 策略的第一步。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowDeviceAuthAsPrimaryForDomainJoinedDevices
允许将设备身份验证作为已加入域的设备的主要认证方式。


```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ClientAuthenticationMethods
指定客户端身份验证方法。

```yaml
Type: ClientAuthenticationMethod
Parameter Sets: (All)
Aliases:
Accepted values: None, ClientSecretPostAuthentication, ClientSecretBasicAuthentication, PrivateKeyJWTBearerAuthentication, WindowsIntegratedAuthentication

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DeviceAuthenticationEnabled
指定是否为全局策略启用设备身份验证功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DeviceAuthenticationMethod
指定设备认证方法。

```yaml
Type: DeviceAuthenticationMethod
Parameter Sets: (All)
Aliases:
Accepted values: All, ClientTLS, SignedToken, PKeyAuth

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -PrimaryExtranetAuthenticationProvider
指定一个包含身份验证提供者名称的数组，这些提供者将用于主外部网络，并添加到全局策略中。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PrimaryIntranetAuthenticationProvider
指定一组用于主内网的认证提供程序名称，以便将其添加到全局策略中。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WindowsIntegratedFallbackEnabled
指定是否在内部网中启用回退到集成Windows身份验证的功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-AdfsGlobalAuthenticationPolicy](./Get-AdfsGlobalAuthenticationPolicy.md)

[注册 AdfsAuthenticationProvider](./Register-AdfsAuthenticationProvider.md)

[Get-AdfsAuthenticationProvider](./Get-AdfsAuthenticationProvider.md)

