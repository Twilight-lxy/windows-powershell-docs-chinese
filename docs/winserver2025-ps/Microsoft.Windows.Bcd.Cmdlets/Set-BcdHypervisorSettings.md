---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/set-bcdhypervisorsettings?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BcdHypervisorSettings
---

# Set-BcdHypervisorSettings

## 摘要
{{ 填写剧情简介 }}

## 语法

### SerialWithDebugPort
```
Set-BcdHypervisorSettings [[-Store] <BcdStoreInfo>] [-Baudrate <Int64>] -DebugPort <Int64> [-Serial] [-Force]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 1394
```
Set-BcdHypervisorSettings [[-Store] <BcdStoreInfo>] [-Channel <Int64>] [-Ieee1394] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### NET
```
Set-BcdHypervisorSettings [[-Store] <BcdStoreInfo>] -HostIp <String> -Port <Int64> [-Net] [-Force] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### SerialWithoutDebugPort
```
Set-BcdHypervisorSettings [[-Store] <BcdStoreInfo>] [-Serial] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
{{ 填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在这里添加示例描述 }}

## 参数

### -Baudrate
{{ 填写波特率描述 }}

```yaml
Type: System.Int64
Parameter Sets: SerialWithDebugPort
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Channel
{{ 填写频道描述 }}

```yaml
Type: System.Int64
Parameter Sets: 1394
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DebugPort
{{ 填写调试端口的描述 }}

```yaml
Type: System.Int64
Parameter Sets: SerialWithDebugPort
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
{{ 填充力的描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostIp
{{ 填写主机IP地址的描述 }}

```yaml
Type: System.String
Parameter Sets: NET
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Ieee1394
{{ 填写 Ieee1394 的描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: 1394
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Net
{{ 填写网络描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: NET
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port
{{ 填写端口描述 }}

```yaml
Type: System.Int64
Parameter Sets: NET
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Serial
{{ 填写系列描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SerialWithDebugPort, SerialWithOutDebugPort
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Store
{{ 填写店铺描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdStoreInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdStoreInfo

## 输出

### System.Object
## 备注

## 相关链接
