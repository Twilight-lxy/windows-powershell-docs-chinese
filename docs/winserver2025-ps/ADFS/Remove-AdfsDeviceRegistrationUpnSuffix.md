---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsdeviceregistrationupnsuffix?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsDeviceRegistrationUpnSuffix
---

# 删除 AdFS 设备注册 UPN 后缀

## 摘要
移除自定义的 UPN 后缀。

## 语法

```
Remove-AdfsDeviceRegistrationUpnSuffix [-UpnSuffix] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsDeviceRegistrationUpnSuffix` cmdlet 用于删除自定义用户主体名称（UPN）的后缀。该 cmdlet 会同时移除相应的 UPN 后缀以及与该后缀关联的 SSL 绑定。一旦删除了自定义的 UPN 后缀，使用该后缀的账户将无法再注册设备。若需添加自定义的 UPN 后缀，请使用 `Add-AdfsDeviceRegistrationUpnSuffix` cmdlet。

## 示例

### 示例 1：移除自定义的 UPN 后缀
```
PS C:\> Remove-AdfsDeviceRegistrationUpnSuffix -UpnSuffix "Child.Contoso.com" -Force
```

此命令会从用户用于将其设备连接到工作场所的可接受UPN后缀列表中删除“Child.Contoso.com”这一后缀。

## 参数

### -Force
强制命令运行，而无需请求用户确认。

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

### -UpnSuffix
指定一个 UPN 后缀。该cmdlet会移除您指定的作为有效注册UPN后缀的那个后缀。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

`UpnSuffix` 参数接收字符串对象作为参数值。

## 输出

## 备注

## 相关链接

[Add-AdfsDeviceRegistrationUpnSuffix](./Add-AdfsDeviceRegistrationUpnSuffix.md)

[Get-AdfsDeviceRegistrationUpnSuffix](./Get-AdfsDeviceRegistrationUpnSuffix.md)

[Set-AdfsDeviceRegistrationUpnSuffix](./Set-AdfsDeviceRegistrationUpnSuffix.md)

