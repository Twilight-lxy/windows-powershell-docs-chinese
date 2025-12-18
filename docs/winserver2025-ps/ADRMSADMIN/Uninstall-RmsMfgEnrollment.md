---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/uninstall-rmsmfgenrollment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-RmsMfgEnrollment
---

# 卸载 RmsMfgEnrollment

## 摘要
终止将 AD RMS 服务器与 Microsoft Federation Gateway 的集成过程（即停止该服务器的注册操作）。

## 语法

```
Uninstall-RmsMfgEnrollment [-Force] [-GetDefaultCertificate] [-CertificateThumbprint <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Uninstall-RmsMfgEnrollment` cmdlet 用于终止 Active Directory Rights Management Services (AD RMS) 服务器与 Microsoft Federation Gateway 之间的注册关系。

## 示例

#### 示例 1：使用指定的指纹终止对 Microsoft Federation Gateway 的注册过程
```
PS C:\> Uninstall-RmsMfgEnrollment -CertificateThumbprint "a909502dd82ae41433e6f83886b00d4277a32a7b"
```

该命令使用指定的证书指纹，从 AD RMS 服务器中移除对 Microsoft Federation Gateway 的支持。

### 示例 2：使用默认证书终止注册过程
```
PS C:\> Uninstall-RmsMfgEnrollment -GetDefaultCertificate
```

该命令通过获取并使用 AD RMS 默认证书的证书指纹哈希值，来移除 AD RMS 服务器对 Microsoft Federation Gateway 的支持。

## 参数

### -CertificateThumbprint
指定一个字符串，其中包含用于将 AD RMS 注册到 Microsoft Federation Gateway 的证书的哈希值（即“指纹”）。

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

### -Force
即使存在问题，也会强制完成退订流程。

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
这表示在停止对 AD RMS 服务器的支持并转而使用 Microsoft Federation Gateway 时，需要获取 AD RMS 默认证书的指纹哈希值，并在该过程中使用该哈希值。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[安装 RMS Mfg Enrollment](./Install-RmsMfgEnrollment.md)

