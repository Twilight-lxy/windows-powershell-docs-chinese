---
description: 使用此主题来帮助您使用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/install-rmsmfgenrollment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-RmsMfgEnrollment
---

# 安装 RmsMfgEnrollment

## 摘要
将 AD RMS 服务器注册到 Microsoft Federation Gateway 中。

## 语法

```
Install-RmsMfgEnrollment [-Force] [-GetDefaultCertificate] [-CertificateThumbprint <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Install-RmsMfgEnrollment` 这个 cmdlet 用于将 Active Directory 权限管理服务（AD RMS）服务器注册到 Microsoft Federation Gateway 中。

## 示例

### 示例 1：使用默认证书注册 Microsoft Federation Gateway
```
PS C:\> Install-RmsMfgEnrollment -GetDefaultCertificate
```

该命令通过检索并使用 AD RMS 默认证书的指纹哈希值，将 AD RMS 集群注册到 Microsoft Federation Gateway 中。

### 示例 2：使用指定的证书注册到 Microsoft Federation Gateway
```
PS C:\> Install-RmsMfgEnrollment -CertificateThumbprint "a909502dd82ae41433e6f83886b00d4277a32a7b"
```

该命令使用非默认证书的指纹哈希值，将 AD RMS 集群注册到 Microsoft Federation Gateway 中。

## 参数

### -CertificateThumbprint
指定一个字符串，其中包含用于向 Microsoft Federation Gateway 注册的证书的指纹哈希值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -GetDefaultCertificate
这表示需要获取 AD RMS 默认证书的指纹哈希值，并使用该哈希值来注册 Microsoft Federation Gateway。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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

### 无

## 输出

### 无

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[卸载-RmsMfgEnrollment](./Uninstall-RmsMfgEnrollment.md)

