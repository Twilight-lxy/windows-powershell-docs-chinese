---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmscertchain?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsCertChain
---

# Get-RmsCertChain

## 摘要
生成一份关于AD RMS集群中特定用户请求的证书链的报告。

## 语法

```
Get-RmsCertChain -RequestId <Int64> [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsCertChain` cmdlet 会生成一份关于 Active Directory 权限管理服务 (AD RMS) 集群中特定用户请求的证书链的报告。

要获取报告，请指定您希望获取报告的用户请求的 RequestID，然后将 *Path* 参数设置为 AD RMS 提供程序驱动器路径 `<PSDrive>:\`Report，其中 `<PSDrive>` 是提供程序驱动器的 ID。您也可以指定相对路径。例如，点（.）表示当前位置。

使用 **Get-RmsUserRequestReport** cmdlet 来获取您想要获取证书链报告的用户请求的 RequestID。

## 示例

#### 示例 1：通过 ID 获取证书链
```
PS C:\> Get-RmsCertChain -Path "." -RequestId 100
```

此命令会显示编号为100的请求的证书链。

### 示例 2：传入用户请求 ID 以获取其证书链
```
PS C:\> Get-RmsUserRequestReport -Path "." -RequestType GetClientLicensorCertificate -UserId 1 | Get-RmsCertChain -Path "."
```

此命令使用 **Get-RmsUserRequestReport** cmdlet 来获取用户请求的 ID，然后将该 ID 传递给 **Get-RmsCertChain** cmdlet 以显示该请求的证书链。

## 参数

### -Confirm
在运行cmdlet之前会提示您确认是否要执行该操作。

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

### -Path
指定一个提供程序驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，并且没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RequestId
用于指定用户请求的唯一内部ID。

```yaml
Type: Int64
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[如何使用 Windows PowerShell 与 AD RMS 进行配合](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsCertInfo](./Get-RmsCertInfo.md)

[Get-RmsChildCert](./Get-RmsChildCert.md)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

