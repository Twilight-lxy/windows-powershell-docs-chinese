---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmsrequestinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsRequestInfo
---

# Get-RmsRequestInfo

## 摘要
生成关于AD RMS集群中特定用户请求的报告。

## 语法

```
Get-RmsRequestInfo -RequestId <Int64> [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsRequestInfo` cmdlet 会生成一份关于 Active Directory 权限管理服务（AD RMS）集群中特定用户请求的报告。

要获取报告，请指定您希望获取报告的用户请求的*RequestID*，然后将*Path*参数设置为 AD RMS 提供程序驱动器的子路径 `<PSDrive>:\`Report`，其中 `<PSDrive>` 是提供程序驱动器 ID。您也可以指定一个相对路径。例如，点（.）表示当前位置。

使用 `Get-RmsUserRequestReport` cmdlet 来获取您希望获取详细报告的用户请求的 *RequestID*。

## 示例

### 示例 1：获取指定的用户请求
```
PS C:\> Get-RmsRequestInfo -Path "." -RequestID 1000
```

这个命令会显示有关特定用户请求的信息。

### 示例 2：按类型获取用户请求
```
PS C:\> Get-RmsUserRequestReport -Path "." -RequestType AcquireLicense -UserID 1 | Get-RmsRequestInfo -Path "."
```

此命令会显示有关用户获取许可证请求的详细信息。`Get-RmsUserRequestReport` cmdlet 会检索用户的许可证请求，然后将结果传递给 `Get-RmsRequestInfo` cmdlet 以显示该请求的详细内容。

## 参数

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

### -Path
指定提供者驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，且没有默认值。

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
指定用户请求的唯一内部ID。

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

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

